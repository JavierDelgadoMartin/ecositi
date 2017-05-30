import { Component, OnInit } from '@angular/core';
import { ApiServiceService } from '../api-service.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  private username = "";
  private password = "";
  constructor(private service:ApiServiceService) { }
  

  ngOnInit() { }

  logInUser(){
    var token;
    if (this.username != "" || this.password != ""){
      token = this.service.login(this.username,this.password);
      console.log(token);
    }
  }
}
