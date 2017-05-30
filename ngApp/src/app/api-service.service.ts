import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
import {Observable, Subject} from 'rxjs/Rx';


@Injectable()
export class ApiServiceService {
  private token : Subject<any> = new Subject<any>();
  private link = "http://127.0.0.1:8000/perfil/";
  constructor(private ajax:Http) { }

  login(user,pass): Observable<any>{
    this.getToken(user,pass);
    return this.token.asObservable();
    }
    getToken(username,password){
    var data = JSON.stringify({username: username,password: password});
    this.ajax.get(this.link)
    .map(response => response.json())
    .subscribe(data =>this.token.next(data))
  }
}
