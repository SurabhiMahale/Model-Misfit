import { useState } from 'react'
import './styles/style.css'
import Header from './components/Header'
import Sidebar from './components/Sidebar'
import Home from './components/Home'
// import Login from './pages/Login'
import Webcamcomponet from './components/Webcamcomponet'
function App() {
  const [openSidebarToggle, setOpenSidebarToggle] = useState(false)

  const OpenSidebar = () => {
    setOpenSidebarToggle(!openSidebarToggle)
  }

  return (
    <div className='grid-container'>
      <Header OpenSidebar={OpenSidebar}/>
      <Sidebar openSidebarToggle={openSidebarToggle} OpenSidebar={OpenSidebar}/>
      <Home />
      {/* <Webcamcomponet/> */}
    </div>
    // <Login/>
  )
}

export default App;

