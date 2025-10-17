# Robot pozíció szimuláció
## A publisher véletlen (x, y) pozíciókat küld, a subscriber kiszámolja a távolságot az origótól.

A package két node-ból áll. A /position_publisher random x és y koordinátákat hirdet a /position topic-ra amiket a /position_subscriber fogad és kiszámolja milyen messze vanak az origótól a koordináták, majd azokat kiirja a konzolra. Megvalósítás ROS 2 Humble alatt.
