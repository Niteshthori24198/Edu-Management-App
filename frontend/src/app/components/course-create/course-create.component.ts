import { Component, OnInit } from '@angular/core';
import { FormGroup, Validators, FormBuilder } from '@angular/forms';
import { CourseService } from 'src/app/services/course.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-course-create',
  templateUrl: './course-create.component.html',
  styleUrls: ['./course-create.component.css'],
})
export class CourseCreateComponent implements OnInit {
  courseForm!: FormGroup;

  constructor(
    private fb: FormBuilder,
    private courseServices: CourseService,
    private router: Router,
  ) {}

  ngOnInit(): void {
    this.initializeForm();
  }

  initializeForm(): void {
    this.courseForm = this.fb.group({
      course_code: ['', Validators.required],
      course_name: ['', Validators.required],
      department: ['', Validators.required],
      credits: ['', Validators.required],
      description: ['', Validators.required],
    });
  }

  onSubmit(): void {
    if (this.courseForm.invalid) return;
    // console.log(this.courseForm.value);
    this.createCourse();
  }

  createCourse(): void {
    this.courseServices.createCourse(this.courseForm.value).subscribe(
      (res) => {
        // console.log(res);
        alert('Course created successfully');
        this.router.navigate([
          '/dashboard',
          { outlets: { d: ['courses'] } },
        ]);
      },
      (err) => {
        alert('Error creating course');
        console.log(err);
      },
    );
  }
}
