import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms'
import { ReactiveFormsModule } from '@angular/forms';
import { FormGroup, FormControl } from '@angular/forms'

@Component({
  selector: 'app-userdetails',
  templateUrl: './userdetails.component.html',
  styleUrls: ['./userdetails.component.css']
})
export class UserdetailsComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }
   Form1 = new FormGroup({

name1: new FormControl(),
email1 : new FormControl(),
mob1 : new FormControl(),

})

 get()
{
  console.log(this.Form1.value)
//   if(this.Form1.value.name1 == 'Harshi' && this.Form1.value.pass1=='1234')
//   {
//     alert("Authenticated User")
//   }
//   else{
//     alert("Not a Valid User")
//   }
 }
}
