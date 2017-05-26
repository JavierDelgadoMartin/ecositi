import { Component, OnInit } from '@angular/core';
import {FormControl} from '@angular/forms';

import 'rxjs/add/operator/startWith';
import 'rxjs/add/operator/map';

@Component({
  selector: 'app-register-user',
  templateUrl: './register-user.component.html',
  styleUrls: ['./register-user.component.css']
})
export class RegisterUserComponent implements OnInit {
  stateCtrl: FormControl;
  filteredStates: any;

  states = [
    'Andalucía',
    'Aragón',
    'Islas Baleares',
    'Canarias',
    'Cantabria',
    'Castilla-La Mancha',
    'Castilla y León, Cataluña',
    'Comunidad de Madrid',
    'Comunidad Foral de Navarra',
    'Comunidad Valenciana',
    'Extremadura',
    'Galicia',
    'País Vasco',
    'Principado de Asturias',
    'Región de Murcia',
    'La Rioja'
  ];


  ngOnInit() {}

}
