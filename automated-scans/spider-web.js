const zapClient = require('zap-clientapi');

// Configuration options for the ZAP scanner
const options = {
    apiKey: 'your_api_key_here',
    target: 'http://your-web-app-url.com',
    spider: {
        maxDepth: 5,
        maxDuration: 5,
        acceptCookies: true,
        handleODataParametersVisited: true,
        ignoreRobotsTxt: false
    }
};

// Start the ZAP scanner
zapClient.createClient('localhost', 8080, function (err, client) {
    if (err) {
        console.log('Failed to connect to ZAP API:', err);
        return;
    }

    // Launch the spider
    console.log('Spidering target URL...');
    client.spider.scan(options.target, options.spider, function (err, scanId) {
        if (err) {
            console.log('Spider scan failed:', err);
            return;
        }

        // Poll the spider status until it completes
        console.log('Spidering in progress...');
        pollSpiderStatus(scanId, function () {
            // Launch the active scan
            console.log('Scanning target URL for vulnerabilities...');
            client.ascan.scan(options.target, '', '', '', '', '', '', function (err, scanId) {
                if (err) {
                    console.log('Active scan failed:', err);
                    return;
                }

                // Poll the active scan status until it completes
                console.log('Scanning in progress...');
                pollActiveScanStatus(scanId, function () {
                    console.log('Scan complete!');
                    client.core.alerts(options.target, '', function (err, alerts) {
                        if (err) {
                            console.log('Failed to retrieve alerts:', err);
                            return;
                        }

                        console.log(`Found ${alerts.length} vulnerabilities:`);
                        alerts.forEach(alert => {
                            console.log(`- ${alert.name} (${alert.risk})`);
                        });
                    });
                });
            });
        });
    });
});

// Poll the spider status until it completes
function pollSpiderStatus(scanId, callback) {
    console.log('Checking spider status...');
    setTimeout(function () {
        zapClient.ascan.status(scanId, function (err, status) {
            if (err) {
                console.log('Failed to retrieve spider status:', err);
                return;
            }

            if (status == '100') {
                console.log('Spidering complete!');
                callback();
            } else {
                pollSpiderStatus(scanId, callback);
            }
        });
    }, 10000);
}

// Poll the active scan status until it completes
function pollActiveScanStatus(scanId, callback) {
    console.log('Checking scan status...');
    setTimeout(function () {
        zapClient.ascan.status(scanId, function (err, status) {
            if (err) {
                console.log('Failed to retrieve scan status:', err);
                return;
            }

            if (status == '100') {
                console.log('Scanning complete!');
                callback();
            } else {
                pollActiveScanStatus(scanId, callback);
            }
        });
    }, 10000);
}
