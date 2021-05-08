import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { toast } from 'react-toastify';
import axiosMain from '../../http/axios/axios_main';
import Sidebar from '../../components/Sidebar/Sidebar';
import Header from '../../components/Header/Header';

const Profile = () => {

    const [data, setData] = useState([]);
    const [errValue, setErrValue] = useState();

    useEffect(() => {
        getUserProfile();
    }, []);

    const getUserProfile = () => {
        const userId = localStorage.getItem('userId');
        console.log("UserId", userId);
        axiosMain
            .get('/user/' + userId + '/')
            .then(response => {
                if (response.status === 200) {
                    console.log("RESPONSE", response)
                    setData(response.data);
                    toast.success(`User Profile Fetch Successful`, {
                        position: 'top-right',
                        autoClose: 3000,
                        hideProgressBar: true,
                        closeOnClick: true,
                        pauseOnHover: true,
                        draggable: true,
                        progress: undefined,
                    });
                }
            })
            .catch(error => {
                setErrValue(error);
                console.error('Error', error);
                setErrValue("This User Profile Fetch Failed")
            });
    };



    return (
        <React.Fragment>
            <Header />
            <Sidebar />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <div className="content-body">
                <div className="container">
                    <div className="row">
                        <div className="col-xxl-6 col-xl-6 col-lg-6">
                            <div className="card welcome-profile">
                                <div className="card-body">
                                    <img src="./images/profile/2.png" alt="" />
                                    <h4>Welcome, {data.username}</h4>
                                    <p>Looks like you are not verified yet. Verify yourself to use the full potential of
                                    bookstagram.</p>
                                    <ul>
                                        <li>
                                            <a href="#">
                                                <span className="verified"><i className="icofont-check-alt"></i></span>
                                                Verify account
                                             </a>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                        {/* <div className="col-xxl-6 col-xl-6 col-lg-6">
                            <div className="card">
                                <div className="card-header">
                                    <h4 className="card-title">Download App</h4>
                                </div>
                                <div className="card-body">
                                    <div className="app-link">
                                        <h5>Get Verified On Our Mobile App</h5>
                                        <p>Verifying your identity on our mobile app more secure, faster, and reliable.</p>
                                        <a href="#" className="btn btn-primary">
                                            <img src="./images/android.svg" alt="" />
                                        </a>
                                        <br />
                                        <div className="mt-3"></div>
                                        <a href="#" className="btn btn-primary">
                                            <img src="./images/apple.svg" alt="" />
                                        </a>
                                    </div>
                                </div>
                            </div>
                        </div> */}

                        <div className="col-xxl-12">
                            <div className="card">
                                <div className="card-header">
                                    <h4 className="card-title">Information </h4>
                                    <Link to="/settings-profile" className="btn btn-primary">Edit</Link>
                                </div>
                                <div className="card-body">
                                    <form className="row">
                                        <div className="col-xxl-4 col-xl-4 col-lg-4 col-md-6">
                                            <div className="user-info">
                                                <span>USER NAME</span>
                                                <h4>{data.username}</h4>
                                            </div>
                                        </div>
                                        <div className="col-xxl-4 col-xl-4 col-lg-4 col-md-6">
                                            <div className="user-info">
                                                <span>EMAIL ADDRESS</span>
                                                <h4>{data.email}</h4>
                                            </div>
                                        </div>
                                        <div className="col-xxl-4 col-xl-4 col-lg-4 col-md-6">
                                            <div className="user-info">
                                                <span>FIRST NAME</span>
                                                <h4>{data.first_name}</h4>
                                            </div>
                                        </div>
                                        <div className="col-xxl-4 col-xl-4 col-lg-4 col-md-6">
                                            <div className="user-info">
                                                <span>LAST NAME</span>
                                                <h4>{data.last_name}</h4>
                                            </div>
                                        </div>
                                        <div className="col-xxl-4 col-xl-4 col-lg-4 col-md-6">
                                            <div className="user-info">
                                                <span>COUNTRY OF RESIDENCE</span>
                                                <h4>{data.country}</h4>
                                            </div>
                                        </div>
                                        <div className="col-xxl-4 col-xl-4 col-lg-4 col-md-6">
                                            <div className="user-info">
                                                <span>CONTACT</span>
                                                <h4>{data.contact}</h4>
                                            </div>
                                        </div>
                                        <div className="col-xxl-4 col-xl-4 col-lg-4 col-md-6">
                                            <div className="user-info">
                                                <span>WALLET</span>
                                                <h4>{data.wallet}</h4>
                                            </div>
                                        </div>
                                        <div className="col-xxl-4 col-xl-4 col-lg-4 col-md-6">
                                            <div className="user-info">
                                                <span>FRIENDS</span>
                                                <h4>{data.friends}</h4>
                                            </div>
                                        </div>
                                        <div className="col-xxl-4 col-xl-4 col-lg-4 col-md-6">
                                            <div className="user-info">
                                                <span>USER TYPE</span>
                                                <h4>{data.usertype}</h4>
                                            </div>
                                        </div>
                                    </form>

                                </div>
                            </div>
                        </div>

                        <div className="col-xxl-8 col-xl-6">
                            <div className="card">
                                <div className="card-header">
                                    <h4 className="card-title">VERIFY & UPGRADE </h4>
                                </div>
                                <div className="card-body">
                                    <h5>Account Status : <span className="text-warning">Pending <i
                                        className="icofont-warning"></i></span> </h5>
                                    <p>Your account is unverified.
                                </p>
                                    <a href="#" className="btn btn-primary"> Get Verified</a>
                                </div>
                            </div>
                        </div>
                        <div className="col-xxl-4 col-xl-6">
                            <div className="card">
                                <div className="card-header">
                                    <h4 className="card-title">Earn 30% Commission </h4>
                                </div>
                                <div className="card-body">
                                    <p>Refer books to your friends and earn 30% of their sale.</p>
                                    <a href="#" className="btn btn-primary"> Referral Program</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

        </React.Fragment>
    );

}

export default Profile;
