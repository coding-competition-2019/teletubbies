import { Component, OnInit } from '@angular/core';
import {AuthService} from '../../services/auth.service';
import {NgForm} from '@angular/forms';

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

  constructor(private authService: AuthService) { }

  ngOnInit() {
  }

  Submit(f: NgForm) {
    if (f.valid) {
      switch (this.formType) {
        case FormType.SignUp:
          // TODO
          break;
        case FormType.Login:
          // TODO
          break;
      }
    }
  }

}
