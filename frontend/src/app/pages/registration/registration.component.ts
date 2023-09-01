import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { AuthenticationService } from 'src/app/services/authentication.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.css'],
})
export class RegistrationComponent {
  registrationForm!: FormGroup;
  constructor(
    private fb: FormBuilder,
    private auth: AuthenticationService,
    private router: Router,
  ) {}
  ngOnInit(): void {
    this.registrationForm = this.fb.group({
      username: ['', [Validators.required, Validators.minLength(3)]],
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(4)]],
    });
  }
  registerUser() {
    if (this.registrationForm.invalid) {
      return;
    }
    const user = this.registrationForm.value;
    this.auth.register(user).subscribe(
      (res) => {
        // console.log(res);
        alert('Registration successful');
        this.router.navigate(['/']);
      },
      (err) => {
        console.log(err);
      },
    );
  }
}
