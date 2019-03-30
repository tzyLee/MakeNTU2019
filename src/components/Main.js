import React, { Component } from 'react';
import Button from '@material-ui/core/Button';
import ArrowDropUp from '@material-ui/icons/ArrowDropUp';
import ArrowDropDown from '@material-ui/icons/ArrowDropDown';
import LibraryBooks from '@material-ui/icons/LibraryBooks';
import './Main.scss';
// import Reader from './Reader.jsx';

class Main extends Component {
  constructor(props) {
    super(props);
    this.handleFlipPage = this.handleFlipPage.bind(this);
    this.state = { page: 'Press Flip Page to view next page' };
  }

  handleSaveText() {
    fetch('/save', { method: 'GET' });
  }

  handleFlipPage() {
    fetch('/page', { method: 'POST' })
      .then(resp => resp.json())
      .then(data => this.setState({ page: data['page'] }));
    this.setState({ page: 'Fetching ...' });
  }

  handleRead() {
    fetch('/read', { method: 'GET' });
  }

  render() {
    return (
      <div id="top">
        <div id="pageContainer">
          <div id="textBox" className="animated fadeIn delay-2s">
            <p>{this.state.page}</p>
          </div>
        </div>
        <div id="buttonContainer">
          <div id="innerButtonContainer" className="animated fadeIn delay-2s">
            <Button className="button" onClick={this.handleSaveText}>
              Save Text
            </Button>
            <Button className="button" onClick={this.handleFlipPage}>
              Flip Page
            </Button>
            <Button className="button" onClick={this.handleRead}>
              Read Page
            </Button>
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
