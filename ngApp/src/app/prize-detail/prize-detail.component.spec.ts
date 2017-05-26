import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PrizeDetailComponent } from './prize-detail.component';

describe('PrizeDetailComponent', () => {
  let component: PrizeDetailComponent;
  let fixture: ComponentFixture<PrizeDetailComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PrizeDetailComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PrizeDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
