import { Component, OnInit } from '@angular/core';
import {AuthService} from '../../services/auth.service';
import {NgForm} from '@angular/forms';
import {HttpClient} from '@angular/common/http';
import {map} from 'rxjs/operators';

enum FormType {
  Login = 1,
  SignUp = 2
}

@Component({
  selector: 'app-auth',
  templateUrl: './auth.component.html',
  styleUrls: ['./auth.component.scss']
})
export class AuthComponent implements OnInit {

  FormType = FormType;

  formType: FormType = FormType.SignUp;
  username = '';
  password = '';

  constructor(private authService: AuthService, private http: HttpClient) { }

  ngOnInit() {
  }

  async Submit(f: NgForm) {
    if (f.valid) {
      switch (this.formType) {
        case FormType.SignUp:
          // this.http.post('http://127.0.0.1:5000/login', {msg: 'sdf'}).pipe(map((x: any) => x.success === 0));          break;
        case FormType.Login:
          // this.http.post('http://127.0.0.1:5000/login', {msg: 'sdf'}).pipe(map((x: any) => x.success === 0));          break;
      }
    }
  }

}
