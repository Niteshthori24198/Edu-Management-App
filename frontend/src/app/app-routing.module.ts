import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './pages/login/login.component';
import { RegistrationComponent } from './pages/registration/registration.component';
import { DashboardComponent } from './pages/dashboard/dashboard.component';
import { WelcomeComponent } from './pages/welcome/welcome.component';
import { InstructorComponent } from './pages/instructor/instructor.component';
import { authGuard } from './guards/auth.guard';
import { ProfileComponent } from './components/profile/profile.component';
import { CoursesComponent } from './pages/courses/courses.component';
import { CourseCreateComponent } from './components/course-create/course-create.component';

const routes: Routes = [
  { path: '', component: LoginComponent },
  { path: 'register', component: RegistrationComponent },
  {
    path: 'dashboard',
    canActivate: [authGuard],
    component: DashboardComponent,
    children: [
      { path: '', redirectTo: 'profile', pathMatch: 'full' },
      { path: 'profile', component: ProfileComponent, outlet: 'd' },
      { path: 'courses', component: CoursesComponent, outlet: 'd' },
      { path: 'course-create', component: CourseCreateComponent, outlet: 'd' },
    ],
  },
  { path: 'welcome', component: WelcomeComponent },
  // { path: 'student', canActivate: [authGuard], component: StudentComponent },
  {
    path: 'instructor',
    canActivate: [authGuard],
    component: InstructorComponent,
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
