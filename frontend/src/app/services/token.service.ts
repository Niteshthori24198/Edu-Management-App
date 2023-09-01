import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { environment } from 'src/environments/environment.development';
const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json',
    "Authorization":
      'Token ' + JSON.parse(localStorage.getItem('token') || '{}')?.token,
  }),
};

@Injectable({
  providedIn: 'root',
})
export class TokenService {
  private baseUrl = environment.apiUrl;
  constructor(private http: HttpClient) {}
  checkToken(): Observable<any> {
    return this.http.get<any>(`${this.baseUrl}/api/test-token`, httpOptions);
  }
}
