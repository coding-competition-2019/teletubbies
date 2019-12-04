import {Component, OnDestroy, OnInit} from '@angular/core';
import {AuthService} from '../../services/auth.service';
import {Subscription} from 'rxjs';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss']
})
export class NavbarComponent implements OnInit, OnDestroy {

  opened = false;

  isLoggedIn: boolean = null;
  isLoggedInSub: Subscription;

  constructor(private authService: AuthService) { }

  ngOnInit() {
    this.isLoggedInSub = this.authService.IsLoggedIn.subscribe(x => {
      this.isLoggedIn = x;
    });
  }

  ngOnDestroy(): void {
    this.isLoggedInSub.unsubscribe();
  }

}
