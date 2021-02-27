import React from "react";
import { Route, Switch, BrowserRouter } from "react-router-dom";

import MainPage from "./components/MainPage";
import Upload from "./components/Upload";


function App() {
  return (
    <div className="root">
      <BrowserRouter>
        <Switch>
          <Route exact path="/" component={MainPage}></Route>
          <Route path="/admin/upload" component={Upload}></Route>
        </Switch>
      </BrowserRouter>
    </div>
  );
}

export default App;
