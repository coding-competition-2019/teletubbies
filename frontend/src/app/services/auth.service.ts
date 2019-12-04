import { Injectable } from '@angular/core';
import {Observable, of} from 'rxjs';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  public get IsLoggedIn(): Observable<boolean> {
    return of(true);
  }

  constructor(private http: HttpClient) { }

}
