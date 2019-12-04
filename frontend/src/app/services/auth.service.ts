import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  public get IsLoggedIn(): boolean {
    return false;
  }

  constructor() { }

}
