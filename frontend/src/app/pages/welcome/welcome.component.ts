import { Component } from '@angular/core';
import { Router } from '@angular/router';
@Component({
  selector: 'app-welcome',
  templateUrl: './welcome.component.html',
  styleUrls: ['./welcome.component.css'],
})
export class WelcomeComponent {
  instructor = localStorage.getItem('instructor');
  constructor(private router: Router) {}
  ngOnInit(): void {
    if (this.instructor) {
      this.router.navigate(['/dashboard']);
    }
  }
}
