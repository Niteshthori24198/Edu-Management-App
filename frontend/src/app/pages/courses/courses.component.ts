import { Component } from '@angular/core';
import { Course } from '../../types/Course';
import { CourseService } from 'src/app/services/course.service';

@Component({
  selector: 'app-courses',
  templateUrl: './courses.component.html',
  styleUrls: ['./courses.component.css'],
})

export class CoursesComponent {
  courses!: Course[];
  constructor(private courseService: CourseService) {
  }
  ngOnInit(): void {
    this.getCourses();
  }
  getCourses(): void {
    this.courseService.getCourses().subscribe((res: any) => {
      this.courses = res.data;
      // console.log(this.courses);
    });
  }
}
