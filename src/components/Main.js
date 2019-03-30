import React, { Component } from 'react';
import Button from '@material-ui/core/Button';
import ArrowDropUp from '@material-ui/icons/ArrowDropUp';
import ArrowDropDown from '@material-ui/icons/ArrowDropDown';
import LibraryBooks from '@material-ui/icons/LibraryBooks';
import './Main.css';
import Reader from './Reader.jsx';

class Main extends Component {
  render() {
    return (
      <div id="top">
        <div id="pageContainer">
          <div id="textBox" className="animated fadeIn delay-2s">
            <Reader />
          </div>
        </div>
        <div id="buttonContainer">
          <div id="innerButtonContainer" className="animated fadeIn delay-2s">
            <Button className="button">Save Text</Button>
            <Button className="button">Flip Page</Button>
            <Button className="button">Read Page</Button>
            <div id="upDownButtonContainer">
              <Button className="button">
                <ArrowDropUp />
              </Button>
              <Button className="button">
                <ArrowDropDown />
              </Button>
            </div>
          </div>
          <div id="logo">
            Lazy
            <LibraryBooks
              id="icon"
              className="animated infinite bounce delay-1s"
            />
            rEEd
          </div>
        </div>
      </div>
    );
  }
}

export default Main;
