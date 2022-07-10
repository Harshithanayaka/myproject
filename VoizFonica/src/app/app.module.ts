import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { ApiService } from './app.service';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
// import { PlansComponent } from './plans/plans.component';
// import { UserdetailsComponent } from './userdetails/userdetails.component';
import { FormsModule } from '@angular/forms'
// import { ReactiveFormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent,
    //PlansComponent,
    //UserdetailsComponent
  ],
  imports: [
    BrowserModule,
//     AppRoutingModule,
      FormsModule,
//     ReactiveFormsModule
     HttpClientModule,
  ],
  providers: [ApiService],
  bootstrap: [AppComponent],
})
export class AppModule { }
