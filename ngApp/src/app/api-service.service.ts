import { Injectable } from '@angular/core';
import { Http,RequestOptions,Headers } from '@angular/http';
import {Observable, Subject} from 'rxjs/Rx';


@Injectable()
export class ApiServiceService {
  private token : Subject<any> = new Subject<any>();
  private link = "http://127.0.0.1:8000";
  constructor(private ajax:Http) { }

  login(user,password): Observable<any>{
    let url = "/rest_auth/login/";
    var data = JSON.stringify({username: user,password: password});
    this.getToken(data,url);
    return this.token.asObservable();
  }
  
  getToken(data,url){
    let headers = new Headers({"content-type": "application/json"});
    let options = new RequestOptions({ headers: headers});
    this.ajax.post(this.link+url,data,options)
    .map(response => response.json())
    .subscribe(data =>this.token.next(data))
  }

  register(username,password,firstname,lastname,email,date,city,state,postalCode){
    let url = "/rest_auth/registration"
    var data = JSON.stringify({username: username,password1: password,password2: password});
    this.getToken(data,url);
    this.createPerfil(username,password,firstname,lastname,email,date,city,state,postalCode)
  }

  createPerfil(username,password,firstname,lastname,email,date,city,state,postalCode){
    var data = JSON.stringify({username: username,password: password,
      firstname: firstname,lastname: lastname,city: city,state: state,birth_date: date});
    let headers = new Headers({"content-type": "application/json"});
    let options = new RequestOptions({ headers: headers});
    this.ajax.post(this.link+"/perfil/",data,options)
    .map(response => response.json())
  }
}
