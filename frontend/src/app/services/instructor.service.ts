import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { environment } from 'src/environments/environment.development';
import { Instructor } from '../types/Instructor';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' }),
};

type IdNumberOrUndefined = number | undefined;

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
  getById(id: IdNumberOrUndefined): Observable<any> {
    return this.http.get<Instructor>(`${this.baseUrl}/${id}`);
  }
  update(id: IdNumberOrUndefined, instructor: Instructor) {
    return this.http.put<Instructor>(
      `${this.baseUrl}/${id}/update`,
      instructor,
      httpOptions,
    );
  }
}
