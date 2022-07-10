import { Component, OnInit} from '@angular/core';
import { ApiService } from './app.service';
//import { Item } from './list.interface';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'VoizFonica';
  items: any;
  error:any;
// constructor(private router: Router){}
// gotoHome(){
// this.router.navigate(['/userdetails.component.html'])
// }

constructor(private api: ApiService){}
ngOnInit() : void{
this.get();
}
  get=()=>{
  this.api.getItems().subscribe(
  data=> { this.items=data;},
  );
       (error : any) => this.error = error

     }

getvalue(value){
  console.log(value)

  }

}
