package com.iv.innovations.vendor;

import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class VendorController {

    @Autowired
    private VendorRepository vendorRepository;

    @GetMapping("/vendors")
    public List<Vendor> getAllVendors() {
        return vendorRepository.findAll();
    }
}
