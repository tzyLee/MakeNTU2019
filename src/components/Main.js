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
    this.handleRead = this.handleRead.bind(this);
    this.state = {
      page: 'Press Flip Page to view next page',
      lastIdx: 0,
      lineIdx: 0,
      highlighted: []
    };
    this.sep = new RegExp(/[,.]\s/);
  }

  handleSaveText() {
    fetch('/save', { method: 'GET' });
  }

  handleFlipPage() {
    fetch('/page', { method: 'POST' })
      .then(resp => resp.json())
      .then(data =>
        this.setState({
          page: data['page']
        })
      );
    this.setState({
      page: 'Fetching ...',
      lastIdx: 0,
      lineIdx: 0,
      highlighted: []
    });
  }

  handleRead() {
    fetch('/read', {
      body: JSON.stringify({
        lastIdx: this.state.lastIdx,
        lineIdx: this.state.lineIdx
      }),
      method: 'POST'
    })
      .then(
        resp => (
          console.log(resp.status),
          resp.status === 200 ? Promise.reject('End of read') : resp.json()
        )
      )
      .then(data => {
        let endIndex = data['lastIdx'];
        // Highlight lastIdx ~ endIndex - 1
        let highlight = [
          this.state.page.substring(0, this.state.lastIdx),
          <span className="hightlight">
            {this.state.page.substring(this.state.lastIdx, endIndex)}
          </span>,
          this.state.page.substring(endIndex)
        ];
        this.setState({ highlighted: highlight });
        this.setState(data);
        this.handleRead(); // Recursive call
      })
      .catch(err => {
        if (err !== 'End of read') throw err;
        // Rethrow unexpected error
        else this.setState({ lastIdx: 0, lineIdx: 0, highlighted: [] }); // Reset state
      });
  }

  handleUpButton(){
    fetch('/up', { method: 'POST'});
  }

  handleDownButton(){
    fetch('/down', { method: 'POST'})
  }

  render() {
    return (
      <div id="top">
        <div className={this.state.page == 'Fetching ...' ? "pageContainer__waiting":"pageContainer"}>
          <div id="textBox" className="animated fadeIn delay-2s">
            <p>
              {this.state.highlighted.length
                ? this.state.highlighted
                : this.state.page}
            </p>
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
              <Button className="button" onClick={this.handleUpButton}>
                <ArrowDropUp />
              </Button>
              <Button className="button" onClick={this.handleDownButton}>
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
