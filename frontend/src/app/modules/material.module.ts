import { NgModule } from '@angular/core';
import {
  MatButtonModule,
  MatIconModule,
  MatMenuModule,
  MatCardModule,
  MatInputModule,
  MatDividerModule
  /* MatCheckboxModule,
  MatInputModule,
  MatCardModule,
  MatGridListModule,
  MatToolbarModule,
  MatListModule,
  MatPaginatorModule,
  MatTableModule,
  MatExpansionModule,
  MatSnackBarModule,
  MatDialogModule,
  MatProgressSpinnerModule,
  MatSortModule,
  MatTabsModule,
  MatSelectModule,
  MatProgressBarModule,
  MatRadioModule,
  MatButtonToggleModule,
  MatChipsModule,
  MatRippleModule */
} from '@angular/material';
// import {DragDropModule} from '@angular/cdk/drag-drop';

const modules = [
  MatButtonModule,
  MatIconModule,
  MatMenuModule,
  MatCardModule,
  MatInputModule,
  MatDividerModule
  /*MatButtonModule,
  MatCheckboxModule,
  MatInputModule,
  MatGridListModule,
  MatToolbarModule,
  MatListModule,
  MatPaginatorModule,
  MatIconModule,
  MatTableModule,
  MatExpansionModule,
  MatSnackBarModule,
  MatDialogModule,
  MatProgressSpinnerModule,
  MatSortModule,
  MatTabsModule,
  MatSelectModule,
  MatProgressBarModule,
  MatRadioModule,
  MatButtonToggleModule,
  DragDropModule,
  MatChipsModule,
  MatRippleModule*/
];

@NgModule({
  imports: modules,
  exports: modules
})

export class MaterialModule { }
