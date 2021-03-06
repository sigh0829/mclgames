
def goplot(fname):
    d = genfromtxt("%s.log" % (fname))
    figure(figsize=(8,12))
    subplot(3,1,1)
    plot(d[:,3], 'r-')
    plot(d[:,5], 'b.-')
    xlabel('TRIAL NUMBER')
    ylabel('X DEV (pixels)')
    title(fname)
    subplot(3,1,2)
    plot(d[:,4], 'r-')
    plot(d[:,6], 'b.-')
    xlabel('TRIAL NUMBER')
    ylabel('TIMING (sec)')
    subplot(3,1,3)
    plot(d[:,5],d[:,6],'b.-')
    plot(d[:,3],d[:,4],'ro')
    plot(d[0,5],d[0,6],'go')
    plot(d[-1,5],d[-1,6],'bo')
    xlabel('XDEV (pixels)')
    ylabel('TIMING (sec)')
    grid('on')
