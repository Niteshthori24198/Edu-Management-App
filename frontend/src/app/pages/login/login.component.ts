import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthenticationService } from 'src/app/services/authentication.service';
import { TokenService } from 'src/app/services/token.service';

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
    private tokenService: TokenService,
  ) {}

  ngOnInit(): void {
    this.tokenService.checkToken().subscribe((res) => {
      if (res.status == 200) {
        // this.router.navigate(['/welcome']);
      }
    });

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
    this.auth.login(user).subscribe(
      (res) => {
        if (res) {
          // console.log(res);
          localStorage.setItem('token', JSON.stringify(res));
        }
        alert('Login successfully');
        this.router.navigate(['/welcome']);
      },
      (err) => {
        alert('Login failed, please try again');
      },
    );
  }
}
