import { Injectable } from '@angular/core';
import {Observable, of} from 'rxjs';
import {HttpClient} from '@angular/common/http';
import {map} from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  public get IsLoggedIn(): Observable<boolean> {
    return this.http.post('http://127.0.0.1:5000/login', {}).pipe(map((x: any) => x.success === 0));
  }

  constructor(private http: HttpClient) { }

}
