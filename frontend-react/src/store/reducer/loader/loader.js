import * as actionLabels from '../../actionLabels';

export const INITIAL_STATE = {
  loader: false,
};

export default (state = INITIAL_STATE, action) => {
  switch (action.type) {
    case actionLabels.ON_SHOW_LOADER:
      return {
        ...state,
        loader: true,
      };

    case actionLabels.ON_HIDE_LOADER:
      return {
        ...state,
        loader: false,
      };

    default:
      return state;
  }
};
