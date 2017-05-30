import { Component, OnInit,Input } from '@angular/core';
import { ApiServiceService } from '../api-service.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  constructor(private service:ApiServiceService) { }
  private username;
  private password = 'mojon';
  private token;

  ngOnInit() {
  }

  logInUser(){
    this.token = this.service.login(this.username,this.password);
  }
}
