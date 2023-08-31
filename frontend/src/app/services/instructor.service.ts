import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { environment } from 'src/environments/environment.development';
import { Instructor } from '../Instructor';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' }),
};

@Injectable({
  providedIn: 'root',
})
export class InstructorService {
  private baseUrl = environment.instructorUrl;
  constructor(private http: HttpClient) {}
  create(instructor: Instructor): Observable<any> {
    return this.http.post<Instructor>(
      `${this.baseUrl}/create`,
      instructor,
      httpOptions,
    );
  }
}
