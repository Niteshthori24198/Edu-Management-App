import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthenticationService } from 'src/app/services/authentication.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
})
export class LoginComponent implements OnInit {
  loginForm!: FormGroup;
  constructor(
    private fb: FormBuilder,
    private router: Router,
    private auth: AuthenticationService,
  ) {}

  ngOnInit(): void {
    this.loginForm = this.fb.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', Validators.required],
    });
  }
  loginUser() {
    if (this.loginForm.invalid) {
      return;
    }
    // console.log(this.loginForm.value);
    const user = this.loginForm.value;
    this.auth.login(user).subscribe((res) => {
      // console.log(res);
      // delete password from users and same with token into localstorage
      delete user.password;
      res = Object.assign(user, res)
      if (res) {
        console.log(res);
        localStorage.setItem('token', JSON.stringify(res));
      }
      alert('Login successfull');
      this.router.navigate(['/welcome']);
    });
  }
}
