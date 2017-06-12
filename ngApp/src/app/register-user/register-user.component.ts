import { Component, OnInit } from '@angular/core';
import { ApiServiceService } from '../api-service.service';

@Component({
  selector: 'app-register-user',
  templateUrl: './register-user.component.html',
  styleUrls: ['./register-user.component.css']
})
export class RegisterUserComponent implements OnInit {
  private username = "";
  private firstname = "";
  private lastname = "";
  private password = "";
  private email = "";
  private date = "";
  private city = "";
  private state = "";
  private postalcode;

  constructor(private service:ApiServiceService) { }

  ngOnInit() {}

  registerUser(){
    this.service.register(this.username,this.password,this.firstname,this.lastname,
      this.email,this.date,this.city,this.state,this.postalcode);
  }
}
