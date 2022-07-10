import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable(
{ providedIn: 'root'
})
export class ApiService{
api_link: string = 'http://localhost:8000/';
constructor(private http: HttpClient){ }
//READ
getItems() {
   return this.http.get(this.api_link + 'api/list/');
  }
  //UPDATE
  //DELETE
  //CREATE
}
