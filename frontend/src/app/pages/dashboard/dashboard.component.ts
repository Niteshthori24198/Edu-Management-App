import { Component } from '@angular/core';
import { AuthenticationService } from 'src/app/services/authentication.service';
import { Router } from '@angular/router';
@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css'],
})
export class DashboardComponent {
  user: any = JSON.parse(localStorage.getItem('token') || '{}');
  constructor(
    private auth: AuthenticationService,
    private router: Router,
  ) {}
  ngOnInit(): void {}
  logout() {
    console.log('logout');
    this.auth.logout()?.subscribe((res) => {
      this.router.navigate(['/']);
    });
  }
}
