import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from "react-redux";

import profileImage from '../../assets/images/profile/2.png';
import Sidebar from '../../components/Sidebar/Sidebar';
import { hideLoader, onLogout } from '../../store/actions';
import { Link } from 'react-router-dom';
import axiosMain from '../../http/axios/axios_main';
import { toast } from 'react-toastify';

Object.size = function(obj) {
    var size = 0,
      key;
    for (key in obj) {
      if (obj.hasOwnProperty(key)) size++;
    }
    return size;
  };

const Header = () => {
    const userData = JSON.parse(localStorage.getItem('userData'));

    const [notificationData, setNotificationData] = useState([]);
    const [profileDropdown, setProfileDropdown] = useState(false);
    const [errValue, setErrValue] = useState();
    const [notify, setNotify] = useState();

    const [notificationDropdown, setNotificationDropdown] = useState(false);
    const dispatch = useDispatch();
    const data = useSelector(state => state);
    const dp = localStorage.getItem('dp');
    const email = localStorage.getItem('email');

    useEffect(() => {
        if(localStorage.getItem('notification')!= undefined){
            setNotify(localStorage.getItem('notification'));
        } else {
            setNotify(0);
        }
        getTickerNotification();
    }, [notify]);

    const getTickerNotification = () => {
        const userId = localStorage.getItem('userId');

        axiosMain
            .get('/userfeed/?pk=' + userId, {
                notify_type: "Ticker Notification"
            })
            .then(response => {
                if (response.status === 200) {
                    console.log("Response",  Object.size(response.data) )
                    setNotificationData(response.data);
                    toast.success(`User Books Fetch Successful`, {
                        position: 'top-right',
                        autoClose: 3000,
                        hideProgressBar: true,
                        closeOnClick: true,
                        pauseOnHover: true,
                        draggable: true,
                        progress: undefined,
                    });
                }
                console.log("Notify", notify);
                localStorage.setItem('notification', Object.size(response.data) - notify);
            })
            .catch(error => {
                setErrValue(error);
                console.error('Error', error);
                setErrValue("This Books Fetch Failed")
            });
    };

    const logout = () => {
        localStorage.clear();
        dispatch(onLogout())
        dispatch(hideLoader())

        window.location.href = '/';
    };

    return (
        <React.Fragment>
            <div className='header'>
                <div className='container'>
                    <div className='row'>
                        <div className='col-xxl-12'>
                            <div className='header-content'>
                                <div className='header-right'>
                                    <div className='brand-logo'>
                                        <a href='index.html'>
                                            <img src='./images/logo.png' alt='' />
                                            <span>Bookstagram</span>
                                        </a>
                                    </div>
                                    <div className='search'>
                                        <form action='#'>
                                            <div className='input-group'>
                                                <input type='text' className='form-control' placeholder='Search Here' />
                                                <span className='input-group-text'>
                                                    <i className='icofont-search'></i>
                                                </span>
                                            </div>
                                        </form>
                                    </div>
                                </div>

                                <div className='header-right'>
                                    <div className='dark-light-toggle' onclick={() => console.log('Toggle Clicked')}>
                                        <span className='dark'>
                                            <i className='icofont-moon'></i>
                                        </span>
                                        <span className='light'>
                                            <i className='icofont-sun-alt'></i>
                                        </span>
                                    </div>
                                    {/* <div className='header-right'>
                                    <span>
                                        <p>{notify}</p>
                                    </span>
                                    </div> */}
                                    <div className='notification dropdown'>
                                        <div className='notify-bell' onClick={() => notificationDropdown ? setNotificationDropdown(false) : setNotificationDropdown(true)}>
                                            <span>
                                                <i className='icofont-alarm'></i>
                                            </span>
                                        </div>
                                        { notificationDropdown ? 
                                        <div className='dropdown-menu dropdown-menu-right notification-list'>
                                                <h4>Announcements</h4>
                                        {notificationData.length >= 1 && notificationData.map(({ publist, comments, authorJSON, buyerJSON, bookJSON }, index) => (
                                           
                                                <div className='lists'>
                                                    <a href='#' className=''>
                                                        <div className='d-flex align-items-center'>
                                                            <span className='mr-3 icon success'>
                                                                <i className='icofont-check'></i>
                                                            </span>
                                                            {comments === "Book Bought Ticker" ?
                                                            <div>
                                                                <p>{comments}</p>
                                                                <br/>
                                                                <p>{buyerJSON.first_name} {buyerJSON.last_name} Bought book {bookJSON.name} from {authorJSON.first_name} {authorJSON.last_name} </p>
                                                                <span>{publist}</span>
                                                            </div> :  
                                                            <div>
                                                                <p>{comments}</p>
                                                                <br/>
                                                                <p>Bought book </p>
                                                                <span>{publist}</span>
                                                            </div>}
                                                        </div>
                                                    </a>
                                                    {/* <a href='#' className=''>
                                                        <div className='d-flex align-items-center'>
                                                            <span className='mr-3 icon fail'>
                                                                <i className='icofont-close'></i>
                                                            </span>
                                                            <div>
                                                                <p>2FA verification failed</p>
                                                                <span>2020-11-04 12:00:23</span>
                                                            </div>
                                                        </div>
                                                    </a> */}
                                                    {/* <a href='#' className=''>
                                                        <div className='d-flex align-items-center'>
                                                            <span className='mr-3 icon pending'>
                                                                <i className='icofont-warning'></i>
                                                            </span>
                                                            <div>
                                                                <p>Phone verification pending</p>
                                                                <span>2020-11-04 12:00:23</span>
                                                            </div>
                                                        </div>
                                                    </a> */}
{/* 
                                                    <a href='./settings-activity.html'>
                                                        More <i className='icofont-simple-right'></i>
                                                    </a> */}
                                                </div>
                                            ))}
                                    </div>: null}
                                    </div>
                                                
                                    
                                    <div className='profile_log dropdown'>
                                        <div className='user' onClick={() => profileDropdown ? setProfileDropdown(false) : setProfileDropdown(true)}>
                                            <span className='thumb'>
                                                <img src={dp} alt='profile' />
                                            </span>
                                            <span className='arrow'>
                                                <i className='icofont-angle-down'></i>
                                            </span>
                                        </div>
                                        {profileDropdown ?
                                            <div className='dropdown-menu dropdown-menu-right'>
                                                <div className='user-email'>
                                                    <div className='user'>
                                                        <span className='thumb'>
                                                            <img src={dp} alt='profile' />
                                                        </span>
                                                        <div className='user-info'>
                                                            <span>{email}</span>
                                                        </div>
                                                    </div>
                                                </div>
                                                <Link
                                                    to='/profile'
                                                    className='dropdown-item'
                                                >
                                                    <i className='icofont-ui-user'></i>Profile
                                                 </Link>
                                                <Link
                                                    to='/settings-profile'
                                                    className='dropdown-item'
                                                >
                                                    <i className='icofont-ui-settings'></i>Settings
                                                 </Link>
                                                <a className='dropdown-item logout' onClick={() => logout()}>
                                                    <i className='icofont-logout'></i> Logout
                                                </a>
                                            </div> : null
                                        }
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <Sidebar />
        </React.Fragment >
    );
};

export default Header;
