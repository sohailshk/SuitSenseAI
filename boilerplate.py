marker_boilerplate = """var marker = new google.maps.marker.AdvancedMarkerElement({
position: {lat: markerData.lat, lng: markerData.lng},
map: map,
title: markerData.name + ' - ' + markerData.address
});

// Add content to marker
const content = document.createElement('div');
content.innerHTML = markerData.name;
content.style.color = '#1976d2';
content.style.fontWeight = 'bold';
content.style.fontSize = '12px';
marker.content = content;
"""

holding_period_boilerplate = """

WITH sale_deltas AS (
    SELECT 
        cs1.condo_unit_id, 
        cs1.closing_date AS current_closing_date, 
        cs2.closing_date AS previous_closing_date,
        (cs1.closing_date - cs2.closing_date) AS delta_days
    FROM 
        core_condosale cs1
    JOIN 
        core_condosale cs2 
    ON 
        cs1.condo_unit_id = cs2.condo_unit_id 
    WHERE 
        cs1.closing_date > cs2.closing_date
        AND cs1.blacklist = FALSE
        AND cs2.blacklist = FALSE
        AND cs2.closing_date = (
            SELECT MAX(cs3.closing_date)
            FROM core_condosale cs3
            WHERE cs3.condo_unit_id = cs1.condo_unit_id
            AND cs3.closing_date < cs1.closing_date
            AND cs3.blacklist = FALSE
        )
        AND cs1.condo_unit_id IN (
            SELECT id 
            FROM core_condounit 
            WHERE blacklist = FALSE 
            AND building_id IN (
                SELECT id 
                FROM core_condobuilding 
                WHERE market_id = (
                    SELECT id FROM core_condomarket WHERE name = 'Brickell'
                )
            )
        )
)
SELECT 
    AVG(delta_days) AS average_delta
FROM 
    sale_deltas;



"""

two_bed_holding_period_boilerplate = """


WITH sale_deltas AS (
    SELECT 
        cs1.condo_unit_id, 
        cs1.closing_date AS current_closing_date, 
        cs2.closing_date AS previous_closing_date,
        (cs1.closing_date - cs2.closing_date) AS delta_days
    FROM 
        core_condosale cs1
    JOIN 
        core_condosale cs2 
    ON 
        cs1.condo_unit_id = cs2.condo_unit_id 
    WHERE 
        cs1.closing_date > cs2.closing_date
        AND cs1.blacklist = FALSE
        AND cs2.blacklist = FALSE
        AND cs2.closing_date = (
            SELECT MAX(cs3.closing_date)
            FROM core_condosale cs3
            WHERE cs3.condo_unit_id = cs1.condo_unit_id
            AND cs3.closing_date < cs1.closing_date
            AND cs3.blacklist = FALSE
        )
        AND cs1.condo_unit_id IN (
            SELECT id 
            FROM core_condounit 
            WHERE blacklist = FALSE 
            AND beds = 2
            AND building_id IN (
                SELECT id 
                FROM core_condobuilding 
                WHERE market_id = (
                    SELECT id FROM core_condomarket WHERE name = 'Brickell'
                )
            )
        )
)
SELECT 
    AVG(delta_days) AS average_delta
FROM 
    sale_deltas;


"""

javascript_map_boilerplate = """
function initMap() {
    // Check if Google Maps API is available
    if (typeof google === 'undefined' || !google.maps) {
        console.error('Google Maps API not loaded');
        return;
    }

    var locations = [
        // Building and school markers will be listed here
    ];

    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 13,
        center: {lat: [average_lat], lng: [average_lng]},
        mapId: 'DEMO_MAP_ID' // Required for AdvancedMarkerElement
    });

    var bounds = new google.maps.LatLngBounds();

    locations.forEach(function(location) {
        var position = {lat: location.lat, lng: location.lng};
        
        var marker = new google.maps.marker.AdvancedMarkerElement({
            position: position,
            map: map,
            title: location.label
        });
        
        // Create custom content for marker
        const content = document.createElement('div');
        content.innerHTML = location.label;
        content.style.color = '#1976d2';
        content.style.fontWeight = 'bold';
        content.style.fontSize = '12px';
        content.style.backgroundColor = 'white';
        content.style.padding = '4px 8px';
        content.style.borderRadius = '4px';
        content.style.border = '1px solid #ccc';
        marker.content = content;
        
        bounds.extend(position);
    });

    // Fit map to show all markers
    if (locations.length > 0) {
        map.fitBounds(bounds);
    }
}

// Initialize map when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    if (document.getElementById('map')) {
        initMap();
    }
});
"""

building_marker_format_boilerplate = "{lat: [building.lat], lng: [building.lon], label: '[building.alt_name] - [building.address]'}"

school_marker_format_boilerplate = "{lat: [school.geometry.location.lat], lng: [school.geometry.location.lng], label: '[school.name]'}"