import * as actionLabels from '../../actionLabels';

const initialState = {
  username: '',
  password: '',
  authToken: localStorage.getItem('userToken'),
  userData: JSON.parse(localStorage.getItem('userData')),
  isLogin: false,
};

export default (state = initialState, action) => {
  switch (action.type) {
    case actionLabels.LOGIN_REQUEST_SUCCESS: {
      console.log("testtt", action.payload)
      return {
        ...state,
        username: '',
        password: '',
        authToken: action.payload.userToken,
        userData: action.payload.userData,
        isLogin: true,
      };
    }
    case actionLabels.LOGIN_REQUEST_FAIL: {
      return {
        ...state,
        username: '',
        password: '',
        authToken: null,
        userData: null,
        isLogin: false,
      };
    }
    case actionLabels.DESTROY_SESSION:
      return {
        ...state,
        username: '',
        password: '',
        authToken: null,
        userData: null,
        isLogin: false,
      };
    default:
      return state;
  }
};
