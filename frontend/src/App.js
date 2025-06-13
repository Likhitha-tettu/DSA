import Test from "./components/Test";
import {Routes, Route, Link, BrowserRouter} from 'react-router-dom';

function App(){
    // <div className="App">
    //   <h1>React Django</h1>
    //   <Test />
    // </div>
  return(
  <BrowserRouter>
  <Routes>
    <Route path ="/" element={<Test />} />
  </Routes>
  </BrowserRouter>
  )
}

export default App;