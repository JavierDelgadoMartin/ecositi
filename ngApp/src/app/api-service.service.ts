import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
import {Observable, Subject} from 'rxjs/Rx';


@Injectable()
export class ApiServiceService {
  
  constructor(private ajax:Http) { }

  login(username,password){
    return this.ajax.post('http://127.0.0.1:8000/rest-auth/login/',{
    "username": username,
    "password": password})
    .map(response => response.json())
  }
}
