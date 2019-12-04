import { NgModule } from '@angular/core';

import { Routes, RouterModule } from '@angular/router';
import {DashboardComponent} from '../components/dashboard/dashboard.component';
import {AuthComponent} from '../components/auth/auth.component';
import {AuthGuard} from '../guards/auth.guard';

// components



const routes: Routes = [
  { path: '', component: DashboardComponent, canActivate: [AuthGuard] },
  { path: 'auth', component: AuthComponent /*, canActivate: [AuthGuard]*/ },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class RoutingModule { }
export const RoutingComponents = [
  DashboardComponent
];
