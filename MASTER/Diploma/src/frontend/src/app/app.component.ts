import { Component } from '@angular/core';
import {range} from 'lodash';


enum Modes {
  FU1 = 'FU1',
  FU2 = 'FU2',
  FU3 = 'FU3',
  FU4 = 'FU4'
}

const BAUD_RATES: number[] = [
  1200,
  2400,
  4800,
  9600,
  19200,
  38400,
  57600,
  115200
];

const POWER: number[] = range(1, 8 + 1);

@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.scss']
})
export class AppComponent {
  public readonly MODES: string[] = Object.keys(Modes);
  public readonly BAUD_RATES: number[] = BAUD_RATES;
  public readonly POWER: number[] = POWER;
  public config = false;
  public mode: Modes = Modes.FU1;
  test() {
    console.log('test');
    console.log(this.config);
  }
}
