# TPER GTFS Feeds

This repository automatically downloads and stores the latest GTFS feeds for the Bologna bus network provided by TPER.

Three feeds are downloaded daily: `gommagtfsbo`, `gommagtfsfe`, `gtfsmex`.
Files are named as `gtfs_<name>_latest.zip`, as well as `gtfs_tper_clean.zip`, which contains a cleaned up version of all three datasets using `gtfstidy`.

## Usage

You can directly download the latest GTFS feed from this repository:

- `gtfs_gommagtfsbo_latest.zip`
- `gtfs_gommagtfsfe_latest.zip`
- `gtfs_gtfsmex_latest.zip`


Each file corresponds to the respective feed from TPER.

## License

The original GTFS feeds are provided under the Creative Commons Attribuzione 3.0 Italia (CC BY 3.0 IT) license by TPER [[1](https://creativecommons.org/licenses/by/3.0/it),[2](https://solweb.tper.it/web/tools/open-data/open-data-legal.aspx)].

This repository automates the download of the feeds; the license of the original data still applies.
