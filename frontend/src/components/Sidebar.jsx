import React from 'react'

 
 import { BsExclamationCircleFill, BsGrid1X2Fill, BsFillArchiveFill, BsFillCameraVideoFill } from 'react-icons/bs';
 import { MdSecurity } from "react-icons/md";
 import { TbSettingsFilled } from "react-icons/tb";
 import RiskScore from './RiskScore';

function Sidebar({openSidebarToggle, OpenSidebar}) {
  return (
    <aside id="sidebar" className={openSidebarToggle ? "sidebar-responsive": ""}>
        <div className='sidebar-title'>
            <div className='sidebar-brand'>
                <MdSecurity  className='icon_header'/> WatchTower AI
            </div>
            <span className='icon close_icon' onClick={OpenSidebar}>X</span>
        </div>

        <ul className='sidebar-list'>
            <li className='sidebar-list-item'>
                <a href="/">
                    <BsGrid1X2Fill className='icon'/> Dashboard
                </a>
            </li>
            <li className='sidebar-list-item'>
                <a href="/alert">
                    <BsExclamationCircleFill className='icon'/> Alerts
                </a>
            </li>
            <li className='sidebar-list-item'>
                <a href="#">
                    <BsFillArchiveFill className='icon'/> Reports
                </a>
            </li>
            <li className='sidebar-list-item'>
                <a href="/setting">
                    <TbSettingsFilled className='icon'/> Settings
                </a>
            </li>
            <li className='sidebar-list-item'>
                <a href="/livecam">
                    <BsFillCameraVideoFill className='icon'/> Live Camera
                </a>
            </li>
             <li className='sidebar-list-item'>
                <a href="/Video">
                    <BsFillArchiveFill className='icon'/> Recorded Videos
                </a>
            </li>
        </ul>
        <div className="risk-score-wrapper">
            <RiskScore />
        </div>

        
    </aside>
  )
}

export default Sidebar