import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CourseCreateComponent } from './course-create.component';

describe('CourseCreateComponent', () => {
  let component: CourseCreateComponent;
  let fixture: ComponentFixture<CourseCreateComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [CourseCreateComponent]
    });
    fixture = TestBed.createComponent(CourseCreateComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
