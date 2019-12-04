import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';

import {BrowserAnimationsModule} from '@angular/platform-browser/animations';

// MODELS
import { RoutingModule, RoutingComponents } from './modules/routing.module';
import { MaterialModule } from './modules/material.module';

// COMPONENTS
import { AuthComponent } from './components/auth/auth.component';
import { NavbarComponent } from './components/navbar/navbar.component';
import { FooterComponent } from './components/footer/footer.component';

// SERVICES
import {AuthService} from './services/auth.service';


@NgModule({
  declarations: [
    AppComponent,
    RoutingComponents,
    AuthComponent,
    NavbarComponent,
    FooterComponent
  ],
  imports: [
    BrowserModule,
    RoutingModule,
    MaterialModule,
    BrowserAnimationsModule
  ],
  providers: [AuthService],
  bootstrap: [AppComponent]
})
export class AppModule { }
