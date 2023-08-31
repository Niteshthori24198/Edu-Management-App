import { Component } from '@angular/core';
import { FormBuilder, Validators, FormGroup } from '@angular/forms';
import { Router } from '@angular/router';
import { InstructorService } from 'src/app/services/instructor.service';

@Component({
  selector: 'app-instructor',
  templateUrl: './instructor.component.html',
  styleUrls: ['./instructor.component.css'],
})
export class InstructorComponent {
  instructorForm!: FormGroup;
  alreadyExistEmail: string = JSON.parse(localStorage.getItem('token') || '{}')
    .email;
  constructor(
    private fb: FormBuilder,
    private router: Router,
    private instructorService: InstructorService,
  ) {}
  ngOnInit(): void {
    this.instructorForm = this.fb.group({
      name: ['', [Validators.required]],
      gender: ['', [Validators.required, Validators.minLength(4)]],
      date_of_birth: ['', [Validators.required]],
      department: ['', [Validators.required]],
      email: [this.alreadyExistEmail],
      contact_number: [
        '',
        [
          Validators.required,
          Validators.minLength(10),
          Validators.maxLength(10),
        ],
      ],
    });
  }
  createProfile() {
    if (this.instructorForm.invalid) {
      return;
    }
    const user = this.instructorForm.value;
    console.log(
      '👻 -> file: instructor.component.ts:31 -> InstructorComponent -> createProfile -> user:',
      user,
    );
    this.instructorService.create(user).subscribe((response) => {
      console.log(
        '👻 -> file: instructor.component.ts:33 -> InstructorComponent -> createProfile -> response:',
        response,
      );
      if (response.status == 200) {
        alert('Instructor profile created successfully');
        localStorage.setItem('instructor', JSON.stringify(response.data));
        localStorage.removeItem('student');
      }
      // this.router.navigate(['/dashboard']);
    });
  }
}
