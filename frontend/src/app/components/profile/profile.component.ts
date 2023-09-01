import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { InstructorService } from 'src/app/services/instructor.service';
import { Instructor } from 'src/app/types/Instructor';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css'],
})
export class ProfileComponent implements OnInit {
  UpdateForm!: FormGroup;
  instructorData!: Instructor;
  constructor(
    private fb: FormBuilder,
    private router: Router,
    private instructorService: InstructorService,
  ) {}

  ngOnInit(): void {
    this.fetchAndInitializeForm();
  }

  fetchAndInitializeForm(): void {
    const instructorId = JSON.parse(localStorage.getItem('instructor')!)?.id;
    // console.log(instructorId);
    if (!instructorId) {
      this.router.navigate(['/instructor']);
      return;
    }

    this.instructorService.getById(instructorId).subscribe(
      (res) => {
        this.instructorData = res.data;
        this.initializeForm(res.data);
      },
      (err) => console.error(err),
    );
  }

  initializeForm(data:Instructor): void {
    this.UpdateForm = this.fb.group({
      name: [data.name, Validators.required],
      gender: [
        data.gender,
        [Validators.required, Validators.minLength(4)],
      ],
      date_of_birth: [data.date_of_birth, Validators.required],
      department: [data.department, Validators.required],
      email: [data.email, Validators.required],
      contact_number: [
        data.contact_number,
        [
          Validators.required,
          Validators.minLength(10),
          Validators.maxLength(10),
        ],
      ],
    });
  }

  updateProfile(): void {
    if (this.UpdateForm.invalid) {
      return;
    }
    const confirm = window.confirm('Are you sure you want to update?');
    if (!confirm) return;
    const user = this.UpdateForm.value;
    this.instructorService.update(this.instructorData.id, user).subscribe(
      (res) => {
        localStorage.setItem(
          'instructor',
          JSON.stringify({ id: this.instructorData.id, ...user }),
        );
        alert('Profile Updated Successfully');
      },
      (err) => console.error(err),
    );
  }
}
