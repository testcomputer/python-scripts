package main

import (
    "fmt"
    "net/http"
    "time"

    "github.com/OWASP/zaproxy/client"
)

func main() {
    // Create a new ZAP client
    zapClient, err := client.NewZapClient("http://localhost:8080", time.Second*5)
    if err != nil {
        fmt.Printf("Failed to create ZAP client: %v\n", err)
        return
    }

    // Launch the ZAP spider to crawl the target web application
    scanID, err := zapClient.Spider("http://engineeur.com")
    if err != nil {
        fmt.Printf("Failed to launch ZAP spider: %v\n", err)
        return
    }
    fmt.Printf("ZAP spider scan ID: %s\n", scanID)

    // Wait for the spider to finish
    for {
        status, err := zapClient.SpiderStatus(scanID)
        if err != nil {
            fmt.Printf("Failed to get spider status: %v\n", err)
            return
        }
        if status == "100" {
            fmt.Println("ZAP spider scan completed")
            break
        }
        time.Sleep(time.Second)
    }

    // Launch the ZAP active scan to identify vulnerabilities
    scanID, err = zapClient.ActiveScan("http://engineeur.com")
    if err != nil {
        fmt.Printf("Failed to launch ZAP active scan: %v\n", err)
        return
    }
    fmt.Printf("ZAP active scan ID: %s\n", scanID)

    // Wait for the active scan to finish
    for {
        status, err := zapClient.ActiveScanStatus(scanID)
        if err != nil {
            fmt.Printf("Failed to get active scan status: %v\n", err)
            return
        }
        if status == "100" {
            fmt.Println("ZAP active scan completed")
            break
        }
        time.Sleep(time.Second)
    }

    // Print the vulnerabilities found by ZAP
    alerts, err := zapClient.CoreAlerts("")
    if err != nil {
        fmt.Printf("Failed to get ZAP alerts: %v\n", err)
        return
    }
    fmt.Printf("ZAP identified %d alerts:\n", len(alerts))
    for _, alert := range alerts {
        fmt.Printf("%s: %s\n", alert.Name, alert.Description)
    }
}
