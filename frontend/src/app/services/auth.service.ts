import { Injectable } from '@angular/core';
import {Observable, of} from 'rxjs';
import {HttpClient} from '@angular/common/http';
import {map} from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  public get IsLoggedIn(): Observable<boolean> {
    // return this.http.get('http://127.0.0.1:5000/').pipe(map((x: any) => x.success === 0));
    return of(false);
  }

  constructor(private http: HttpClient) { }

}
