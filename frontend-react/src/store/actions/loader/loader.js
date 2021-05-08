import * as actionLabels from '../../actionLabels';

export const showLoader = () => ({
  type: actionLabels.ON_SHOW_LOADER,
});

export const hideLoader = () => ({
  type: actionLabels.ON_HIDE_LOADER,
});
